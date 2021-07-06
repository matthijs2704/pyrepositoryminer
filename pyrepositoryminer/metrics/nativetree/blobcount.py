from typing import Iterable, List

from pyrepositoryminer.metrics.nativetree.main import NativeTreeMetric
from pyrepositoryminer.metrics.structs import Metric, NativeTreeMetricInput
from pyrepositoryminer.visitableobject import (
    VisitableBlob,
    VisitableObject,
    VisitableTree,
)


class Blobcount(NativeTreeMetric):
    async def analyze(self, tree_tup: NativeTreeMetricInput) -> Iterable[Metric]:
        n = 0
        q: List[VisitableObject] = [tree_tup.tree]
        while q:
            obj = q.pop(0)
            if isinstance(obj, VisitableBlob):
                n += 1
            elif isinstance(obj, VisitableTree):
                q.extend(list(obj))
        return [Metric(self.name, n, False)]
