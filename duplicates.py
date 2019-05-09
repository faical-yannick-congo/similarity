from toolz.curried import curry, compose
import pandas as pd
import numpy as np


apply = curry(pd.DataFrame.apply)
sort_values = curry(pd.DataFrame.sort_values)
all = curry(pd.DataFrame.all)
duplicated = curry(pd.DataFrame.duplicated)
assign = curry(pd.DataFrame.assign)
diff = curry(pd.DataFrame.diff)
npappend = curry(np.append)
npclose = curry(np.allclose)


def sequence(*args):
    return compose(*args[::-1])

@curry
def debug(statement, value):
    print()
    print(statement)
    print(value)
    return value


def find_duplicates(df):
    return df.apply(
        sequence(
            np.array,
            lambda x: x[:-1] == x[1:],
            npappend([False])
        ),
        axis=0)


@curry
def duplicate_if_close(df, atol, rtol):
    return sequence(
        diff,
        apply(func=allclose0(atol, rtol), axis=0)
    )(df)


@curry
def allclose0(atol, rtol, arr):
    return (arr <= atol + rtol * arr)


@curry
def fduplicates(cols, fcols, atol, rtol, df):
    return pd.concat([
        duplicate_if_close(df[fcols], atol, rtol),
        find_duplicates(df[cols])
    ], axis=1)


@curry
def duplicates_allclose(df, dcols, fcols, atol=1e-10, rtol=1e-10):
    """Determine duplicates in dataframe based on tolerances

    Args:
      df: the dataframe
      dcols: the columns that are tested for exact duplicates
      fcols: the columns that are checked for tolerance
      atol: the relative tolerance, can be float or array with length of fcols
      rtol: the absolute tolerance, can be float or array with length of fcols

    This is the similar to `pandas.DataFrame.duplicated` with
    `keep='first'` so only the first duplicate is kept.

    The implementation first uses `pandas.DataFrame.duplicated` on the
    `dcols` argument with `keep=False` to keep all duplicates. The
    duplicate sub-dataframe is then sorted on both `dcols` and
    `fcols`. A diff between each row is then done on the sorted
    duplicates dataframe. The float values are then checked for their
    tolerances. This method may fail is for some edge cases, but
    should in general work well. The edge case will be examined below.

    >>> from toolz.curried import pipe

    Dataframe with 2 duplicates to be removed

    >>> assert pipe(
    ...     dict(
    ...         A=['c', 'c', 'e', 'd', 'd'],
    ...         B=['a', 'a', 'c', 'a', 'a'],
    ...         C=[1, 1.01, 2, 3, 3.01]
    ...     ),
    ...     pd.DataFrame,
    ...     duplicates_allclose(dcols=['A', 'B'], fcols=['C'], atol=0.02),
    ...     npclose([False, True, False, False, True])
    ... )

    Dataframe with 2 duplicates to be removed

    >>> assert pipe(
    ...     dict(
    ...         A=[1,   1,   2,   2, 1],
    ...         B=[2,   2.1, 2,   2, 2],
    ...         C=[3,   3,   2,   2, 3],
    ...         D=[4.5, 4.5, 4.5, 4.6, 4.5]
    ...     ),
    ...     pd.DataFrame,
    ...     duplicates_allclose(dcols=['A', 'B'], fcols=['C', 'D'], atol=0.2),
    ...     npclose([False, False, False, True, True])
    ... )

    """
    func = sequence(
        duplicated(subset=dcols, keep=False),
        lambda x: df[x],
        sort_values(by=dcols + fcols),
        fduplicates(dcols, fcols, atol, rtol),
        apply(func=all, axis=1)
    )

    return df.assign(duplicates=func(df)).duplicates.fillna(False).rename()
